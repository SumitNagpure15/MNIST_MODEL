#!/bin/bash

# Navigate to the inference directory
echo "Navigating to the inference directory..."
cd inference || { echo "Failed to enter 'inference' directory"; exit 1; }

# Build the Docker image
echo "Building the Docker image with tag 'inference_image'..."
docker build -t inference_image . || { echo "Docker image build failed"; exit 1; }

# Run the Docker container with volume and port mappings
echo "Running the Docker container..."
docker run -d -v $(pwd)/../model:/app/model -p 5000:5000 inference_image || { echo "Failed to run the Docker container"; exit 1; }

echo "Docker container is running and accessible on port 4000"
