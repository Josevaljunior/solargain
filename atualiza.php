<?php
function ultimagera(){
    $conexao= new PDO('mysql:host=localhost;dbname=solar_gain','root','');
    $conexao->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $ano= date('Y');
    $mes=date('m');
    $dia=date('d');
    $result= $conexao->query('SELECT * FROM geracao WHERE Ano='.$ano.' AND Mes='.$mes.' AND dia='.$dia.'')->fetchAll();



    $ultimageracao=$result[count($result)-1]['geracao']." Kw";
    return  $ultimageracao;
}

echo ultimagera();



?>