#!/bin/bash

docker build -t eu.gcr.io/test-sa-ki-witt/kafka-producer:latest .
docker push eu.gcr.io/test-sa-ki-witt/kafka-producer:latest