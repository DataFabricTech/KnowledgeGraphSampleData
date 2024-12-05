import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

class AssociationRuleCFRunner:
  def __init__(self, input_data_path, output_data_path):
    self.input_data_path = input_data_path
    self.output_data_path = output_data_path

  def run(self):
    df = pd.read_csv(self.input_data_path)

    if len(df.columns) != 2:
     df = df[df.columns[:2]]
    df.columns = ['userId', 'itemId']

    # 사용자-아이템 매트릭스 생성 (user-item interaction matrix)
    user_item_matrix = df.pivot_table(index='userId', columns='itemId', aggfunc='size', fill_value=0)

    # 아이템 간 코사인 유사도 계산
    item_similarity = cosine_similarity(user_item_matrix.T)

    # 아이템 간 유사도를 데이터프레임으로 변환
    item_similarity_df = pd.DataFrame(item_similarity, 
                                      index=user_item_matrix.columns, 
                                      columns=user_item_matrix.columns)

    # 결과를 ItemId1, ItemId2, Score 형식으로 변환
    item_similarity_melt = item_similarity_df.reset_index().melt(id_vars='itemId', var_name='ItemId2', value_name='Score')

    # 자기 자신과의 유사도(1인 값) 제거
    item_similarity_melt = item_similarity_melt[item_similarity_melt['itemId'] != item_similarity_melt['ItemId2']]
    sorted_df = item_similarity_melt.sort_values(by=['itemId', 'ItemId2'])

    # 칼럼 이름을 itemid에서 antecedent consequent 로 변경
    sorted_df.rename(columns={'itemId': 'antecedent'}, inplace=True)
    sorted_df.rename(columns={'ItemId2': 'consequent'}, inplace=True)

    # Save the association rules to a CSV file
    sorted_df.to_csv(self.output_data_path, index=False)