# Data Fabric 지식그래프 샘플 데이터 처리

> ## 저장소 상태
>
> 본 저장소는 아래 과제의 **1단계(2023~2024)** 지식그래프 구성요소입니다.
> 관계 데이터 간 유사 속성 분석 기능은 2단계에서 Recommender 저장소의
> 유사 속성 탐지 모듈로 계승되었습니다.
>
> - 과제명: 분산된 데이터에 대한 논리적 데이터 통합과 복합분석을 지원하는 데이터 패브릭 기술개발
> - 과제번호: RS-2023-00222191
> - 개발 기간: 2023년 12월 ~ 2024년 12월
> - 계승 저장소: https://github.com/DataFabricTech/Recommender

## 개요

지식그래프 기능 검증에 사용한 샘플 데이터 생성·전처리·분석 코드입니다.
알고리즘 검토 단계의 Jupyter 노트북과, 그 결과를 컨테이너에서 실행하도록 정리한 분석 에이전트로 구성됩니다.

## 저장소 구성

### `2023Demo` — 알고리즘 검토 노트북

| 노트북 | 내용 |
|---|---|
| `Preprocessing.ipynb` | 원시 데이터 전처리입니다. |
| `ClusterAnalysis.ipynb` | 데이터 군집 분석입니다. |
| `RelationAnalysis.ipynb` | 데이터 간 관계 분석입니다. |
| `DO_DOID_Mapping.ipynb`, `DO_DOID_MappingV2.ipynb` | 데이터 객체와 식별자의 매핑 처리입니다. |
| `convergenceUsage/` | 융합 활용 분석을 검토한 코드입니다. 연관규칙(`AssociationRule`), 오토인코더(TensorFlow·PyTorch 두 구현)를 포함합니다. |

### `association-agent` — 연관 분석 에이전트

노트북에서 검토한 연관규칙 분석을 컨테이너에서 실행하기 위한 Python 애플리케이션입니다.

| 디렉터리 | 역할 |
|---|---|
| `generator/` | 분석 입력 데이터를 준비합니다. 모의 데이터 생성(`convergence_data_generator`)과 객체 저장소에서 내려받기(`minio_data_generator`)를 지원합니다. |
| `runner/` | 연관규칙 분석과 협업 필터링 기반 연관 분석을 수행합니다. |
| `common/` | 실행 인자 처리 등 공통 유틸리티입니다. |

## 실행

### 요구 사항

- Python 3.11
- 노트북 실행 시: Jupyter, numpy, pandas

### 분석 에이전트

```bash
cd association-agent
pip install -r requirements.txt
```

모의 데이터로 실행합니다.

```bash
python main.py --mode mock --algorithm association-analysis --analysis_id <분석 식별자>
```

객체 저장소의 데이터로 실행합니다. 접속 정보는 실행 인자로 전달하며, 저장소에 보관하지 않습니다.

```bash
python main.py --mode run --datasource_type MinIO --algorithm association-analysis \
  --analysis_id <분석 식별자> \
  --host <호스트> --port <포트> --region <리전> \
  --bucket_name <버킷> --file_source_path <객체 경로> \
  --access_key <액세스 키> --secret_key <시크릿 키>
```

입력과 결과는 `/pvc/mnt/analysis-<분석 식별자>/` 경로에 CSV로 기록됩니다.
컨테이너 이미지는 `association-agent/Dockerfile`로 빌드합니다.

## 라이선스

Apache License 2.0을 따릅니다. 자세한 내용은 [LICENSE](LICENSE)를 참고하십시오.
