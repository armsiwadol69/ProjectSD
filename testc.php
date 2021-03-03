<html>
<head>
  <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
  <script type="text/javascript">
  <?php
  $serverName = "sql417.main-hosting.eu";
  $userName = "u584979650_siwadol";
  $userPassword = "@Siwadol420";
  $dbName = "u584979650_si_sd";
  $conn = mysqli_connect($serverName,$userName,$userPassword,$dbName);

      if(!$conn){
     die('Could not Connect My Sql:' .mysql_error());
  }

  $sql = "SELECT * FROM rec_used ORDER BY date DESC LIMIT 10";
  $query = mysqli_query($conn,$sql);
  $result = mysqli_query($conn, $sql);
  ?>
    google.charts.load('current', {'packages':['corechart']});
    google.charts.setOnLoadCallback(drawChart);

    function drawChart() {
      var data = google.visualization.arrayToDataTable([
        ['Timestamp', 'Temperature'],
        <?php
        while($row = mysqli_fetch_array($result)) {
        echo "[" ;
        echo $row["date"] . ",";
        echo $row["temp"] . "],";
        };

         ?>

      ]);

      var options = {
        title: 'Company Performance',
        curveType: 'function',
        legend: { position: 'bottom' }
      };

      var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));

      chart.draw(data, options);
    }
  </script>
</head>
<body>
  <div id="curve_chart" style="width: 1920px; height: 1080px"></div>
</body>
</html>
