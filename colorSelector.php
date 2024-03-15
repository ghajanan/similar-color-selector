<?php
include ('color_difference.class.php');

function hex_to_rgb($hex_color) {
    // Converts hex color code to an array of RGB values (0-255).
    $hex_color = ltrim($hex_color, '#');  // Remove leading '#' if present
    return array_map('hexdec', str_split($hex_color, 2));
}

function find_similar_colors($database, $searched_color) {
    // Finds similar colors using the CIEDE2000 color difference formula.
    $searched_rgb = hex_to_rgb($searched_color);
    $distances = [];
    foreach ($database as $color_code) {
        $color_rgb = hex_to_rgb($color_code);
        $distance = (new color_difference())->deltaECIE2000($searched_rgb, $color_rgb);
        $distances[] = array($color_code, $distance);
    }
    usort($distances, function($a, $b) {
        return $a[1] <=> $b[1];
    });
    return $distances;
}
// [black,white,red,blue,aqua,fuchsia,Lime,green,pink,purple,gold,gray]
$colorsArray = ['#000000','#FFFFFF','#FF0000','#0000FF','#00FFFF','#FF00FF',' #00FF00','#008000','#ffc0cb','#800080','#ffd700','#808080'];

$searched_color = '#9fee7f'; 
$length = count($colorsArray);
print($length . "\n");


// $max_distance = 40; // Example threshold

$results_ciede2000 = find_similar_colors($colorsArray, $searched_color);


// print("Similar colors based on CIEDE2000 distance (0 - {$max_distance}):\n");
// foreach ($results_ciede2000 as list($color_code, $distance)) {
//     if (0 <= $distance && $distance <= $max_distance) {  // Filter colors within range
//         print($color_code . ' ' . $distance . "\n");
//     }
// }

// Find the color with the lowest distance
$lowest_distance_color = $results_ciede2000[0]; // Assuming the first element has the lowest distance

// Print the color code with the lowest distance
print("Color with the lowest distance: " . $lowest_distance_color[0] . "\n");

?>
