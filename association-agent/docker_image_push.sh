REGISTRY="192.168.122.128:31234"
IMAGE_NAME="datafabric/agent:20241016_v1"
IMAGE_FULL_NAME="$REGISTRY/$IMAGE_NAME"

docker build -t "$IMAGE_FULL_NAME" .
docker push "$IMAGE_FULL_NAME"