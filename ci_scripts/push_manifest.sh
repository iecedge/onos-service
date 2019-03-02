export IMAGE_TAG=$(cat VERSION)
export DOCKER_CLI_EXPERIMENTAL=enabled

docker manifest create --amend cachengo/onos-synchronizer:$IMAGE_TAG cachengo/onos-synchronizer-x86_64:$IMAGE_TAG cachengo/onos-synchronizer-aarch64:$IMAGE_TAG

docker manifest push cachengo/onos-synchronizer:$IMAGE_TAG
