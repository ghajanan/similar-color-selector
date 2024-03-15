import numpy as np
from skimage.color import deltaE_ciede2000, rgb2lab

def hex_to_rgb(hex_color):
    # Converts hex color code to a tuple of RGB values (0-255).
    hex_color = hex_color.lstrip('#')  # Remove leading '#' if present
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def find_similar_colors_euclidean(database, searched_color):
    # Finds similar colors using Euclidean distance in RGB space.
    searched_rgb = hex_to_rgb(searched_color)

    distances = []
    for color_code in database:
        color_rgb = hex_to_rgb(color_code)
        distance = np.linalg.norm(np.array(searched_rgb) - np.array(color_rgb))
        distances.append((color_code, distance))

    return sorted(distances, key=lambda x: x[1]) 

def find_similar_colors_ciede2000(database, searched_color):
    """Finds similar colors using the CIEDE2000 color difference formula."""

    searched_rgb = np.array(hex_to_rgb(searched_color)).reshape(1, 1, 3) / 255.
    searched_lab = rgb2lab(searched_rgb)

    distances = []
    for color_code in database:
        color_rgb = np.array(hex_to_rgb(color_code)).reshape(1, 1, 3) / 255.
        color_lab = rgb2lab(color_rgb)
        distance = deltaE_ciede2000(searched_lab, color_lab)
        distances.append((color_code, distance[0][0]))

    return sorted(distances, key=lambda x: x[1]) 

# Example usage

database = [
  '#DAD2B5', '#F82836', '#5A3ED2', '#D028CB', '#9253D2', '#86E320',
  '#5267EC', '#1F9501', '#EFEF0B', '#7F7215', '#8D2BC8', '#E50F6E',
  '#58F87C', '#99C6A4', '#17FE1C', '#DA2DC3', '#94E5B6', '#7A3D5C',
  '#D9ACA4', '#FA78F9', '#62CE58', '#84151D', '#E657DF', '#7DE4C1',
  '#9F9F20', '#F0AE36', '#29B95D', '#82719E', '#B52A4E', '#CEC45F',
  '#7C9A65', '#11961A', '#00B2F8', '#1457FF', '#D4AA72', '#87659A',
  '#D6FF7C', '#FBD170', '#5A100E', '#4E25A2', '#16A3FF', '#9A3929',
  '#15F5FA', '#3FB2DC', '#6017B3', '#91E164', '#C67996', '#719279',
  '#7C4B4C', '#D56AC2', '#069516', '#E71ECC', '#5201F0', '#EF6C3A',
  '#6D78BA', '#CDE24E', '#B1C57F', '#D4ADBD', '#2A2D37', '#F82B55',
  '#647A5E', '#42E459', '#062308', '#61FD25', '#0E37EE', '#D2B3A1',
  '#BE00DA', '#BE7591', '#EE0AC9', '#19F7DA', '#8B3953', '#0C9D0A',
  '#D9B14A', '#6B271A', '#05DD5E', '#D5FD3C', '#629368', '#8B3913',
  '#A12408', '#E4CACE', '#6D9503', '#E887AE', '#C9BD42', '#BB1E68',
  '#D7F35E', '#AC91DF', '#738724', '#AF806D', '#DD430B', '#6AEB35',
  '#6CD945', '#82F558', '#CAF8F0', '#F54403', '#F33FF5', '#33E9D4',
  '#BC66C2', '#DEDFD9', '#46E2F5', '#121810','#93C2C4', '#6359AA', 
  '#27EA34', '#E3C024', '#26256C', '#5EC5CA',
  '#893C5B', '#19078B', '#BC8038', '#05F2D3', '#EB023A', '#FF5865',
  '#AB97B8', '#F779C5', '#C79E80', '#933CB9', '#81B365', '#1B7A32',
  '#90733D', '#D5A405', '#6BE25C', '#A5C733', '#4DDB0D', '#E8D3FD',
  '#C400D4', '#E3963D', '#C93FEA', '#F8D956', '#9942C0', '#9A9454',
  '#C7FC26', '#8BBF1A', '#E7962A', '#8CA7E6', '#D98933', '#913A7B',
  '#46D69D', '#15A413', '#4FF99A', '#8EE7EA', '#9E8094', '#E1DE40',
  '#15E632', '#8F7629', '#37F2D7', '#62DB96', '#4096BC', '#C15A7E',
  '#7826DA', '#2BA7C8', '#7E8A5F', '#61515F', '#CA3091', '#FD9610',
  '#C9DB3B', '#2916F5', '#2DA4BF', '#CECE98', '#0F47EB', '#BCFECD',
  '#8F4653', '#2C1A0C', '#EA89B1', '#7A48C1', '#448B0E', '#A93FC8',
  '#35A4A9', '#E0615D', '#28BEFD', '#8DED3F', '#E71FF2', '#49D32F',
  '#F1E255', '#97941E', '#6BBA3D', '#7B6541', '#DECF2D', '#70D0B1',
  '#39B43C', '#F98547', '#326ED8', '#E8A80E', '#313F13', '#2724C9',
  '#A76EC7', '#8DBA19', '#FCCFA9', '#1CBB9C', '#72C6E5', '#042225',
  '#AA4263', '#24D176', '#39E483', '#5D289E', '#FA8D0B', '#4D5B25',
  '#15B419', '#9FEE7F', '#FCBE23', '#B12EBB'
]

# database = ['#000000','#FFFFFF','#FF0000','#0000FF','#FFFF00','#00FFFF','#FF00FF','#00FF00','#0000FF','#008000']

searched_color = '#ffff80' #green
length = len(database)

print(length)

max_distance = 20 # Example threshold

results_euclidean = find_similar_colors_euclidean(database, searched_color)



print("Similar colors based on Euclidean distance (0 - {}):".format(max_distance))
for color_code, distance in results_euclidean:
    if 0 <= distance <= max_distance:  # Filter colors within range
        print(color_code, distance) 

results_ciede2000 = find_similar_colors_ciede2000(database, searched_color)

print("Similar colors based on CIEDE2000 distance (0 - {}):".format(max_distance))
for color_code, distance in results_ciede2000:
    if 0 <= distance <= max_distance:  # Filter colors within range
        print(color_code, distance)


