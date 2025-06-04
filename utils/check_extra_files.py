import os
from google.cloud import storage

local_dir = r'D:\Diploma\data\MC-EIU-audio'
bucket_name = 'mc-eiu-data'
prefix = 'MC-EIU-audio/'

local_files = set()
for root, dirs, files in os.walk(local_dir):
    for file in files:
        rel_path = os.path.relpath(os.path.join(root, file), local_dir).replace("\\", "/")
        local_files.add(rel_path)

client = storage.Client()
bucket = client.bucket(bucket_name)
blobs = bucket.list_blobs(prefix=prefix)

gcs_files = set()
for blob in blobs:
    gcs_path = blob.name[len(prefix):]
    if gcs_path:
        gcs_files.add(gcs_path)

extra_files = gcs_files - local_files

if extra_files:
    print(f"\nFound {len(extra_files)} extra files in GCS not in local folder:")
    for f in sorted(extra_files):
        print(f"- {f}")
else:
    print("\nNo extra files found! ✅")
