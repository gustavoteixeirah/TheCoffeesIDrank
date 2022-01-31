import json
import os


path = os.getcwd()
print("Current path: ", path)

output_path = path + '/each_metadata/'
# Check whether the specified path exists or not
isExist = os.path.exists(output_path)
if not isExist:
    # Create a new directory because it does not exist
    os.makedirs(output_path)
    print("The new directory is created!")


with open("./metadataWithHashes.json", "r") as f:
    metadata = json.load(f)

for tokenMetadata in metadata:
     with open(output_path+str(tokenMetadata['tokenId']), 'w') as outfile:
        json.dump(tokenMetadata, outfile, indent=4)
