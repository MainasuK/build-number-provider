#!/bin/zsh

# Request the build number endpoint and export the result to BUILD_NUMBER
response=$(curl -s -X POST -H "Content-Type: application/json" -d '{"latest_build_number": 1}' http://127.0.0.1:5000/v1/build_number)
echo $response

NEXT_BUILD_NUMBER=$(echo "$response" | grep -oE '"next_build_number"[ ]*:[ ]*[0-9]+' | grep -oE '[0-9]+')
if [ -z "$NEXT_BUILD_NUMBER" ]; then
  BUILD_NUMBER=100
else
  BUILD_NUMBER=$NEXT_BUILD_NUMBER
fi
echo "BUILD_NUMBER=$BUILD_NUMBER"

