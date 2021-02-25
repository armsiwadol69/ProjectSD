<?php
date_default_timezone_set("Asia/Bangkok");
echo date_default_timezone_get();
class dht11{
 public $link='';
 function __construct($temperature, $humidity){
  $this->connect();
  $this->storeInDB($temperature, $humidity);
 }

 function connect(){
  $this->link = mysqli_connect('localhost','u584979650_siwadol','@Siwadol420') or die('Cannot connect to the DB');
  mysqli_select_db($this->link,'u584979650_si_sd') or die('Cannot select the DB');
 }

 function storeInDB($temperature, $humidity){
  $query = "insert into rec_used set temp='".$temperature."', humi='".$humidity."'";
  $result = mysqli_query($this->link,$query) or die('Errant query:  '.$query);
 }

}
if($_GET['t'] != '' and  $_GET['h'] != ''){
 $dht11=new dht11($_GET['t'],$_GET['h']);
}

?>
