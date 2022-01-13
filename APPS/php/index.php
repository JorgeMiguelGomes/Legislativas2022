<?php

function cleanStr($string){
    if(strstr($string, "-")){
        $string=explode("-",$string);
        $string=$string[0];
    }
    if(strstr($string, "–")){
        $string=explode("–",$string);
        $string=$string[0];
    }
    if(strstr($string, "	")){
        $string=explode("	",$string);
        $string=$string[0];
    }
    return trim(mb_strtolower($string, 'UTF-8'));
}

//Composer loading stuff
require __DIR__ . '/../../vendor/autoload.php';
$PDFparser = new \Smalot\PdfParser\Parser();
$pdf = $PDFparser->parseFile(__DIR__ . "/../../PDFS_CNE/legislativas2022_listas_circulos_finais.pdf");
$pages = $pdf->getPages();

$reader = new \PhpOffice\PhpSpreadsheet\Reader\Csv();
$spreadsheet = $reader->load(__DIR__ . "/../../PRODUCTS/legislativas_2022_CNE_all_13JAN2022.csv");

$sheetData = $spreadsheet->getActiveSheet()->toArray(null, false, true, true);
$politicians=array();
foreach($sheetData as $i => $item) {
    if($i>1){
        $circle=$sheetData[$i]['A'];
        $party=$sheetData[$i]['B'];
        $candidate=$sheetData[$i]['C'];
        $type=$sheetData[$i]['D'];
        $candidate=cleanStr($candidate);
        $politicians[$candidate]=$type;
        $politiciansAll[]=$candidate;
    }
}

$missing=array();
foreach ($pages as $page) {
    $text = nl2br($page->getText());
    $text = str_replace(array('&', '%', '$'), ' ', $text);
    $tempPDF = explode('<br />', $text);

    foreach ($tempPDF as $linha => $textolinha) {
        $textolinha=cleanStr($textolinha);
        if($textolinha!=''){
            foreach($politicians as $key => $value){
                if($key!=''){
                    if(strstr($textolinha, $key)){
                        $politiciansExists[]=$textolinha;
                    }
                }
            }
        }
    }
}

//asort($politiciansExists);
//asort($politiciansAll);
$i=0;
$result =  array_diff($politiciansExists, $politiciansAll);
echo "<pre>";
print_r($result);
echo "</pre>";
