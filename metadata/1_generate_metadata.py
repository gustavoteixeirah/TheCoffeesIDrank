import json
import random

# Definição de atributos e raridades
backgrounds = ["The Office", "Beach", "Dark", "Tower", "Company", "Kitchen"]
backgrounds_weights = [35.5, 1.5, 18, 5, 30, 10]

developer = ["Gustavo", "Renan", "Marcelo", "Julien", "V"]
developer_weights = [30, 30, 30, 7.5, 2.5]

beverages = [
    "None",
    "Coffee",
    "Soda",
    "Juice",
    "Energetic",
    "Protein Shake",
    "Tea",
    "Water Bottle",
]
beverages_weights = [10, 40, 13, 5, 15, 1, 0.5, 15.5]

# A soma dos pesos deve ser igual a 100 (100%)
print("Soma dos backgrounds: ", sum(backgrounds_weights))
print("Soma dos developers: ", sum(developer_weights))
print("Soma dos beverages", sum(beverages_weights))

# Define o total de NFTs a ser gerada
TOTAL_NFTs = 100

nfts_attributes = []


def create_trait(trait_type, trait_list, trait_weights):
    trait = {
        "trait_type": trait_type,
        "value": random.choices(trait_list, trait_weights)[0]
    }
    return trait


def generate_nft_attributes():
    attributes = [
        create_trait("Background", backgrounds, backgrounds_weights),
        create_trait("Developer", developer, developer_weights),
        create_trait("Beverage", beverages, beverages_weights)
    ]
    # Valida se os atributos gerados já estão presentes na lista de atributos já gerados
    if attributes in nfts_attributes:
        return generate_nft_attributes()
    else:
        return attributes


# Loop que vai gerar os atributos e armazenar em no array temporário nfts_attributes
for i in range(TOTAL_NFTs):
    new_generated_nft = generate_nft_attributes()
    nfts_attributes.append(new_generated_nft)

# Agora, com os atributos gerados, vamos preencher os demais campos do metadado de cada NFT
metadata = []
for i in range(TOTAL_NFTs):
    # O token id da sua coleção pode começar em 1, que é o caso abaixo, ou em zero (no caso de zero, remover o + 1)
    tokenId = i + 1
    # Aqui você pode personalizar os campos para adequar-se a necessidade da sua coleção
    current_nft_metadata = {
        "name": "KryptoDeveloper #" + str(tokenId),
        "description": "Developers are the key people behind any software that has ever been built. This NFT "
                       "collection seeks to illustrate these hard-working people that expends their days in front of "
                       "a computer to solve problems.",
        "tokenId": tokenId,
        # for the image ipfs hash we need first to generate the image
        # "image": "ipfs://QmPToH9aX8zbK294WAfhsHck1wVtVW3KkJfRz7rxvrzeZE",
        "external_url": "https://www.kryptodevelopers.dev/",
        "attributes": nfts_attributes[i]
    }
    metadata.append(current_nft_metadata)

with open('metadata.json', 'w') as outfile:
    json.dump(metadata, outfile, indent=4)
