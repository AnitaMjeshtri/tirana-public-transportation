import xml.etree.ElementTree as ET
import overpy
import json


def xmlParse(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return root
    except Exception as e:
        print(f"Could not parse {file_path}")


def readFromFile(file_path, destination_file):
    root = xmlParse(file_path)
    api = overpy.Overpass()
    results = []

    if not root:
        return

    relation = root.find('relation')

    if relation is not None:

        for prod in relation.findall('member'):
            ref_result = prod.get('ref')

            if ref_result is not None:
                result = api.query(f"node({ref_result}); out body;")

                if result.nodes:
                    node = result.nodes[0]
                    lat = float(node.lat)
                    lon = float(node.lon)

                    if node.tags != {}:
                        el_dict = {
                            "type": "node",
                            "id": node.id,
                            "lat": lat,
                            "lon": lon,
                            "tags": {tag: str(node.tags[tag]) for tag in node.tags if
                                     (node.tags[tag] != "stop_position")}
                        }
                        results.append(el_dict)

        tag_dict = {
            "additional_tags": {tag.attrib['k']: tag.attrib['v'] for tag in relation.findall('tag')}
        }
        results.append(tag_dict)

    with open(destination_file, "w") as file:
        json_result = json.dumps(results, indent=2)
        file.write(json_result)


if __name__ == '__main__':
    # readFromFile("L16.xml","L16.json")
    # readFromFile("Kombinat-Kinostudio.xml","Kombinat_Kinostudio.json")
    # readFromFile("L2_TegIshStacioniTrenit.xml","L2_TegIshStacioniTrenit.json")
    # readFromFile("L8A_TEG_qender.xml","L8A_TEG_qender.json")
    # readFromFile("L13_Tirana_e_re(Sensi Orar).xml","L13_Tirana_e_re(Sensi Orar).json")
    # readFromFile("L11_PorcelanQender.xml", "L11_PorcelanQender.json")
    # readFromFile("L5B_Qendër_Institut.xml", "L5B_Qendër_Institut.json")
    # readFromFile("L12A_Sharre_UzinaDinamoRe.xml", "L12A_Sharre_UzinaDinamoRe.json")
    # readFromFile("L1A_Allias_Selitë.xml", "L1A_Allias_Selitë.json")
    # readFromFile("L4_CityPark_Qendër.xml", "L4_CityPark_Qendër.json")
    # readFromFile("L8C_SaukiVjetër_Qendër.xml", "L8C_SaukiVjetër_Qendër.json")
    # readFromFile("L3A_Astir_SensiOrar.xml", "L3A_Astir_SensiOrar.json")
    # readFromFile("L8B_Sanatorium_Qendër.xml", "L8B_Sanatorium_Qendër.json")
    readFromFile("xmlFiles/L13_TiranaeRe(Sensi Antiorar).xml", "jsonFiles/L13_TiranaeRe(Sensi Antiorar).json")