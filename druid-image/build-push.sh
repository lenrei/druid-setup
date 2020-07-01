#!/bin/bash

docker build -t eu.gcr.io/test-sa-ki-witt/druid-incubator-mysql:0.16.0-incubating .
docker push eu.gcr.io/test-sa-ki-witt/druid-incubator-mysql:0.16.0-incubating