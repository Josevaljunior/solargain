
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Document</title>
    <script src="https://code.jquery.com/jquery-2.1.1.min.js" type="text/javascript"></script>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
  <script type="text/javascript">
    google.charts.load("current", {packages:['corechart']});
    google.charts.setOnLoadCallback(drawChart);
    
    function drawChart() {
      var data = google.visualization.arrayToDataTable([
        ["Element", "Geração", { role: "style" } ],
        <?php 

$conexao= new PDO('mysql:host=localhost;dbname=solar_gain','root','');
$conexao->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$ano="2024";
$mes="05";
$dia="21";
$result= $conexao->query('SELECT * FROM geracao WHERE Ano='.$ano.' AND Mes='.$mes.' AND dia='.$dia.'')->fetchAll();
$dados=[];
$hora=[];
foreach ($result as $dado){
    $d=floatval($dado['geracao']);
    array_push($dados,$d);
          

}
foreach ($result as $dado){
    $d=strval($dado['hora']);
    array_push($hora,$d);
          

}

for($i=0;$i<count($dados);$i++){
?>
        ["<?= $hora[$i]?>", <?= $dados[$i];?>, "#2E8B57"],

        <?php }?>
      ]);

      var view = new google.visualization.DataView(data);
      view.setColumns([0, 1,
                       { calc: "stringify",
                         sourceColumn: 1,
                         type: "string",
                         role: "annotation", },
                       2]);

      var options = {
        title: "Grafico de geração durante ",
        width: 1000,
        height: 400,
        bar: {groupWidth: "95%"},
        legend: { position: "left" },
      };
      var chart = new google.visualization.AreaChart(document.getElementById('chart_div'));
      chart.draw(view, options);
  }

   
  </script>
  <script>
        $(document).ready(function(){
            setInterval(function(){
                $("#autodata").load('atualiza.php')
            }, 10000);
        });
    </script>
  
</head>
<body>
<header>
        <div class="container-logo">
        <div class="logo-imagem"></div>
        <div class="logo-texto">
            <h1>LOGOTIPO</h1>
        </div>
        </div>
        <div class="menu">
            <ul>
                <li><a href="#">Sobre</a></li>
                <li><a href="#">Login</a></li>
                <li><a href="#">Contato</a></li>
            </ul>

        </div>
    </header>
    
    <div id="chart_div" style="width: 100%; height: 300px;"></div>
    
    <div class="card">
      <div class="tituloPotencia">
        <h1>POTÊNCIA ATUAL</h1>
        <hr>
      </div>
      <img src="inversor desenho.jpg" alt="" height="200" width="200">
      <div id="autodata" class="valor"></div> 
    </div>
</body>
</html>