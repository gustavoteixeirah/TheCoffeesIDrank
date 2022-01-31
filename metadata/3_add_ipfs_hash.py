import json
import re

# READ METADATA
with open("./metadata.json", "r") as f:
    current_metadata = json.load(f)

hashesFile = open("hashes.txt", "r")
hashes = hashesFile.readlines()


hashesList = {}
for line in hashes:
    _hash = re.search(r"(added) (\w+) (\w+).jpg", line).group(2)
    _token_id = re.search(r"(added) (\w+) (\w+).jpg", line).group(3)
    hashesList[_token_id] = _hash

metadata = []
for cm in current_metadata:
    cm["image"] = "ipfs://" + hashesList[str(cm["tokenId"])]
    metadata.append(cm)

with open("metadataWithHashes.json", "w") as outfile:
    json.dump(metadata, outfile, indent=4)
