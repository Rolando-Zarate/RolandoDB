<?php
$version = "1.0 Beta";
class RDBSelect{
	function __construct($filepath){
		$this->filepath = $filepath;
		echo $this->filepath," as database.";
		$this->dbfile = file_get_contents($this->filepath);
		$this->data = json_decode($this->dbfile,true);
	}
	function getRawData(){
		return $this->dbfile;
	}
	function getParsedData(){
		return $this->data;
	}
	function getAllElementsFromObject($name){
		return $this->data[$name];
	}
	function getAllElementsFromObjectIfExists($name){
		if (isset($this->data[$name])){
			return $this->data[$name];		
		}else{			
			
		}
	}
	function createObject($name,$initialelmname,$initialelmcon){
		$this->data[$name] = array($initialelmname=>$initialelmcon);
	}
	function createObjectIfNotExists($name,$initialelmname,$initialelmcon){
		if (isset($this->data[$name])){
			return false;
		}else{
			$this->data[$name] = array($initialelmname=>$initialelmcon);
		}
	}
	function deleteObject($name){
		unset($this->data[$name]);
	}
	function turnDatabaseListToList($list){
		//unused function, php included json parser turn all elements into a multidimensional array.
	}
	function deleteElementFromObject($obj,$name){
		if (count($this->data[$obj])==0){
			echo "All objects must have 1 element minimum.";
		}else{
			unset($this->data[$obj][$name]);
		}		
	}
	function deleteElementFromObjectIfExists($obj,$name){
		if (!isset($this->data[$obj][$name])){
			return false;
		}else{
			if (count($this->data[$obj])==0){
				echo "All objects must have 1 element minimum.";
			}else{
				unset($this->data[$obj][$name]);
			}		
		}
	}
	function refreshData(){
		$this->dbfile = file_get_contents($this->filepath);
		$this->data = json_decode($this->dbfile,true);
	}
	function createDatabase(){
		$this->data = json_decode("{}");
	}
	function commitChanges(){
		file_put_contents($this->filepath,json_encode($this->data));
	}
}
function createNewDatabaseFile($name){
	$file = fopen($name.".rdb", "w") ;
	fwrite($file,"{}");
}
function createNewDatabaseFileIfNotExists($name){
	$checker = file_exists("$name");
	if ($checker){
		
	}else{
		$file = fopen($name.".rdb", "w") ;
		fwrite($file,"{}");
	}
}
function rolandodbVersion(){
	return version;
}
function rolandodbImportantInfo(){
	return "Importatnt Info: This version is just a beta for testing RolandoDB in PHP, so use is recommended in few cases.";
}
?>