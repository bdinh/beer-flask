#!/usr/bin/env bash
./build.sh
ssh ec2-user@ec2-18-223-197-197.us-east-2.compute.amazonaws.com 'bash -s' < update.sh
