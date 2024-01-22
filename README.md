# web-scraping-href-extraction
This repository contains code for web scraping using Selenium to extract a content and images from URL. The technology stack includes AWS Lambda Function, AWS CodeBuild, Selenium library for web scraping, and AWS S3 for storing scraped content.

## Technology

- AWS Lambda Function
- AWS CodeBuild
- Selenium library for Web Scraping
- AWS S3 (Simple Storage Service)

### AWS Lambda Function

The provided Lambda Function utilizes the Selenium library to extract a list of Href from a web page. This list is then prepared for the next step, where each Href will be inserted into and the data will be scraped.

### AWS CodeBuild

AWS CodeBuild is employed to upload the Lambda Function to the AWS platform. It is an AWS service that facilitates the building and deployment of code. CodeBuild handles the uploading of the Lambda Function code to AWS and installs the necessary libraries specified in the `requirements.txt` file, including the Selenium library for web scraping.

### AWS S3

AWS S3 (Simple Storage Service) is used to store the results of the web scraping process. The Lambda Function uploads a CSV file containing the scraped content to an S3 bucket. Additionally, any images extracted during the scraping process are also uploaded to the same S3 bucket.

## Usage

1. Ensure you have the required AWS services set up, including Lambda, CodeBuild, and S3.
2. Configure the Lambda Function to use the Selenium library for web scraping and interact with S3 for storing results.
3. Utilize CodeBuild to upload the Lambda Function code to the AWS platform and install the required libraries from the `requirements.txt` file.
4. Set up an S3 bucket to store the CSV file and scraped images.
