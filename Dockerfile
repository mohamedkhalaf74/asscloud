# Use the official Python image as base
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY cloud.py .
copy random_paragraphs.txt .
# Install dependencies
RUN pip install --no-cache-dir nltk

# Download NLTK stopwords data
RUN python -m nltk.downloader stopwords

# Expose the port your application runs on
EXPOSE 5000

# Run the Python script when the container launches
CMD ["python", "cloud.py"]








