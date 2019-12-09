<?php


function get_json($url)
{}


function get_img_data($url)
{}


function saveImg($data, $file_path)
{}


function fib($num)
{
	if ($num == 0) {return 0;}
	if ($num == 1) {return 1;}
    return fib($num - 1) + fib($num -2);
}


function save_results($text_path, $results){}


function get_baseurl($path){}


function main(){
    $start = time();
    var_dump(fib(40));
    var_dump ((float)time() - (float)$start);
}

main();