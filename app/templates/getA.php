<?php
	header('Access-Control-Allow-Origin: *');
	$f = file_get_contents("answers.txt");
	$arr = explode("\n",$f);
	echo json_encode($arr);
?>