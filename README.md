# avaliativo-aula13
Jean Gonçalves Mello e Diogo Gonçalves Mello

Requisitos:
	Python
	OpenCV nativo
	Endereço da pasta do OpenCV dentro da variável de ambiente "path" (no meu caso o endereço é "C:\Users\User\Desktop\opencv\build\x64\vc14\bin")

Para criar uma IA para detectar gatos precisamos seguir os seguintes passos:
	1. Criar uma pasta do projeto com os códigos "AnalisaTreinamento.py" e "BuildListNegatives.py" e mais duas pastas: "positivas", "negativas" e "treinamnto";

	2. Baixar um dataset de imagens de gatos (quanto mais imagens tiver, mais precisa será a detecção) e colocar dentro da pasta "positivas"(nesse caso foi usado 200 imagens, recomendo usar em torno de 2000 imagens para ter uma boa acertividade);

	3. Colocar imagens que não tenha nenhum gato dentro da pasta "negativas";

	4. Abrir o prompt dentro da pasta do projeto e rodar o "BuildListNegatives.py", isso irá gerar uma lista em .txt das imagens negativas;

	5. No prompt executar o comando:
"opencv_annotation --annotations=saida.txt --images=positivas/"
e selecionar os rostos dos gatos em todas as fotos. Esse comando gera o arquivo "saida.txt", que é uma lista de todos os recortes feitos nas fotos;

	6. No prompt executar o comando:
"opencv_createsamples -info saida.txt -bg negativas.txt -vec vec.vec-w 24 -h 24"
isso gera as amostras para o treinamento;

	7. No prompt executar o comando:
"opencv_traincascade -data treinamento -vec vec.vec-w -bg negativas.txt -numPos 200 -numNeg 450 -w 24 -h 24 -precalcValBufSize 1024 -precalcIdxBufSize 1024 -numStages 30 -acceptanceRatioBreakValue 1.0e-5" isso gera o treinamento em .xml dentro da pasta treinamento (quanto maior o número de estágios mais precisa será a detecção);
	
	8. Rode o código "AnaliseTreinamento.py" com uma imagem com gatos para testar a IA.
