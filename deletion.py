import redis

# Connect to Redis
r = redis.StrictRedis(
    host='redis-12939.c322.us-east-1-2.ec2.cloud.redislabs.com',
    port=12939,
    password='GVBLTziwvl4AvWqgnOJQP8FW6PLU2gDl',
    decode_responses=True  # This allows decoding responses as strings
)

# Specify the key of the record you want to delete
key_to_delete = '2013-04-04'  # Example key, change this to the key of the record you want to delete

# Check if the key exists before deleting
if r.exists(key_to_delete):
    # Delete the record
    r.delete(key_to_delete)
    print(f"Record with key {key_to_delete} deleted successfully.")
else:
    print(f"Record with key {key_to_delete} does not exist.")
