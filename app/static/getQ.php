<?php
	header('Access-Control-Allow-Origin: *');

	extract($_GET);
	$txt = file_get_contents("Q.txt");
	$arr = explode("$$",$txt);
	
	echo $arr[$count];
?>