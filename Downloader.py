#!/usr/bin/env python3
import os, sys
import requests
import re
import argparse
import urllib
import boto3
import botocore
import threading
from urllib.request import urlretrieve

def is_downloadable(url):
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True

def parse_downloadFiles_args():
    parser = argparse.ArgumentParser(description='Configure')    
    parser.add_argument("infile", default=[], nargs='*')
    args = parser.parse_args()
    options = args
    return options.infile 

def get_filename_from_cd(cd):
    if not cd:
        return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    return fname[0]

def split_s3_path(s3_path):
    path_parts=s3_path.replace("s3://","").split("/")
    bucket=path_parts.pop(0)
    key="/".join(path_parts)
    return bucket, key

def download_file_tread(url):    
    file_name = url.split('/')[-1]        
    if url.startswith("s3"):
        print("Downloading from S3 file: %s"%file_name)        
        Bucket, Key = split_s3_path(url)            
        outPutName = file_name
        s3 = boto3.resource('s3')
        try:
            s3.Bucket(Bucket).download_file(Key, outPutName)
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                print ("The object does not exist.")
            else:
                raise        
    elif url.startswith("http"):                                
        if is_downloadable(url):
            print("Downloading from HTTP file: %s"%file_name)        
            with requests.get(url, stream=True) as r:
                with open(file_name, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192): 
                        if chunk: 
                            f.write(chunk)            
                            f.flush()
                            os.fsync(f.fileno())    

if __name__ == "__main__":
    urls = parse_downloadFiles_args()    
    for url in urls:
        t = threading.Thread(target = download_file_tread, args=(url,)).start()
