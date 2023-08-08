from bs4 import *
import requests
import boto3
import uuid
import datetime

# Define env parameters / values
# first hard coded. later move to env parameter in AWS configuration
web_url = "https://www.jamesallen.com/loose-diamonds/oval-cut/1.01-carat-f-color-si1-clarity-sku-18275902"
bucket_name = 'sarine-web-scraping'

# CREATE FOLDER
class web_scraping_to_s3():

    # constructor
    def __init__(self, *args):
        self.url = args[0]
        self.image_arr = []
        self.bucket_name = bucket_name
        self.prefix = ''
        print("url: ", self.url, \
                "Image array: ", self.image_arr, \
                "Bucket name: ", self.bucket_name, \
                "Prefix: ", self.prefix
              )

    # DOWNLOAD ALL IMAGES FROM THAT URL
    def download_images(self):

        # print total images found in URL
        print(f"Total {len(self.image_arr)} Image Found!")

        # checking if images is not zero
        if len(self.image_arr) != 0:

            for i, image in enumerate(self.image_arr):

                # first we will search for "src" in img tag
                try:
                    # Generate a unique value for naming the img
                    unique_id = str(uuid.uuid4())
                    print("Unique ID:", unique_id)

                    image_link = image["src"]
                    print(f"Img url number {i}: {image_link}, with new name: {unique_id}")

                    r = requests.get(image_link).content

                    try:
                        # possibility of decode
                        r = str(r, 'utf-8')

                    except UnicodeDecodeError:

                        # Get the current date
                        current_date = datetime.datetime.now()

                        # Extract year, month, and day
                        year = current_date.year
                        month = current_date.month
                        day = current_date.day

                        # Create the prefix
                        date_path = f"year={year}/month={month:02d}/day={day:02d}/"

                        image_name = f"images{i}_{unique_id}.jpg"
                        self.prefix = f"{date_path}{image_name}"

                        # ingest loaded files to s3
                        downloading_images.dumping_img_files_to_s3(r)

                except:
                    pass


    def dumping_img_files_to_s3(self, image_data):

        try:
            s3_resource = boto3.resource('s3')
            s3_resource.Object(self.bucket_name, self.prefix).put(Body=image_data)
            print(f"Uploaded to S3: {self.prefix}")

        except Exception as e:
            print(f"Error uploading to S3: {e}")


    # extract relevant content from HTML
    def main(self):
        # content of URL
        r = requests.get(self.url)

        # Parse HTML Code
        soup = BeautifulSoup(r.text, 'html.parser')

        # find all images in URL
        self.image_arr = soup.findAll('img')
        print("The url images are: ", self.image_arr)

        # image downloading start
        downloading_images.download_images()


def lambda_handler(event, context):

    ref = event['ref']
    print("The ref is: ", ref)

    # define class
    downloading_images = web_scraping_to_s3(web_url)

    # CALL MAIN FUNCTION
    downloading_images.main()


lambda_handler("", "")