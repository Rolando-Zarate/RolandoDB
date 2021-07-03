<?php
$version = "1.0 Beta 03 07 2021";
class RDBSelect{
	function __construct($filepath){
		$this->filepath = $filepath;
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
			return false;
		}
	}
	function createObject($name){
		$this->data[$name] = array("ignore"=>"ignore");
	}
	function createObjectIfNotExists($name){
		if (isset($this->data[$name])){
			return false;
		}else{
			$this->data[$name] = array("ignore"=>"ignore");
		}
	}
	function deleteObject($name){
		unset($this->data[$name]);
	}
	function deleteElementFromObject($obj,$name){
		unset($this->data[$obj][$name]);
	}
	function deleteElementFromObjectIfExists($obj,$name){
		if (!isset($this->data[$obj][$name])){
			return false;
		}else{
			if (count($this->data[$obj])==0){
				unset($this->data[$name]["ignore"]);
			}else{
				unset($this->data[$obj][$name]);
			}		
		}
	}
	function refreshData(){
		$this->dbfile = file_get_contents($this->filepath);
		$this->data = json_decode($this->dbfile,true);
	}
	function clearDatabase(){
		$this->data = json_decode("{}");
	}
	function commitChanges(){
		file_put_contents($this->filepath,json_encode($this->data));
	}
	function createElementInObject($obj,$elmname,$elmcontent){
		unset($this->data[$obj]["ignore"]);
		$this->data[$obj][$elmname]= $elmcontent;
	}
	function createElementInObjectIfNotExists($obj,$elmname,$elmcontent){
		unset($this->data[$deleteElementFromObjectIfExists]["ignore"]);
		if (isset($this->data[$obj][$elmname])){
			return false;
		}else{
			$this->data[$obj][$elmname]= $elmcontent;
			return true;
		}
	}
	function getElementFromObject($obj,$elm){
		return $this->data[$obj][$elm];
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
?>
