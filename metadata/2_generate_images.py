import json
import os
from PIL import Image

path = os.getcwd()
print("Current path: ", path)

output_path = path + '/images/'
# Check whether the specified path exists or not
isExist = os.path.exists(output_path)
if not isExist:
    # Create a new directory because it does not exist
    os.makedirs(output_path)
    print("The new directory is created!")

# READ METADATA
with open("./metadata.json", 'r') as f:
    metadata = json.load(f)


def generate_image(nft):
    attributes = nft["attributes"]
    image_data = {}
    for attribute in attributes:
        attribute_image = Image.open(
            f'{path}/jpegs/{attribute["trait_type"]}/{attribute["value"]}.png').convert('RGBA')
        image_data[attribute["trait_type"]] = attribute_image

    total_traits = 3
    order = ["Background", "Developer", "Beverage"]

    # Gera inicialmente o composite do primeiro e segundo
    composite = Image.alpha_composite(image_data[order[0]], image_data[order[1]])

    # Itera a partir do terceiro elemento (i + 2) para ir "mesclando" as
    # próximas imagens de acordo com a ordem especificada
    for i in range(total_traits):
        if i >= 2:
            composite = Image.alpha_composite(composite, image_data[order[i]])

    # Converte para RGB
    rgb_composite = composite.convert('RGB')
    # Muda o tamanho conforme necessidade
    resized_image = rgb_composite.resize((512, 512), Image.NEAREST)

    file_name = str(nft["tokenId"]) + ".jpg"
    resized_image.save(output_path + file_name)
    print("Finished generating nft image number ", str(nft["tokenId"]))


for nft_metadata in metadata:
    generate_image(nft_metadata)
