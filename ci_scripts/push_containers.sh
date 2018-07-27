export IMAGE_TAG=$(cat VERSION)
export AARCH=`uname -m`
docker build -f Dockerfile.synchronizer -t cachengo/onos-synchronizer-$AARCH:$IMAGE_TAG .
docker push cachengo/onos-synchronizer-$AARCH:$IMAGE_TAG
