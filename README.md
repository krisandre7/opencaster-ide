# Projeto 2 do Curso de Multiplexação e Transmissão
Crie um programa capaz de editar PMTs, gerando um TS com informações novas. Será possível mudar PIDs de mídias e adicionar novas mídias às PMTs (todas as existentes em um TS). Este programa deve gerar novos valores de CRC adequados aos novos dados. O DVBInspector deve ser capaz de ler os TSs editados (especificamente, as tabelas). Não é necessário encontrar PATs: o DVBInspector pode fornecer o PID das PMTs a serem alteradas.

# Requisitos
É necessário ter o Docker instalado para compilar e executar as ferramentas do projeto pelo container. Para executar os scripts é neccesário conceder permissão de execução a eles:
```
chmod +x build_image.sh
chmod +x run_container.sh
```
Após isso, basta executar o script `./run_container.sh` para criar ou executar o container. 
- Para entrar no container: `docker exec -it opencaster-ide bash`. 
- Para encerrar o container: `docker container stop opencaster-ide`
- Para apagar o container: `docker container rm -f opencaster-ide`
- Para compilar a imagem Docker: ./build_image.sh

# Compilação e Instalação de Ferramentas Opencaster
Após entrar no container utilizando `docker exec -it opencaster-ide bash`, pode-se compilar as ferramentas do opencaster com:
```
cd opencaster/code
make
```
Para instalar, basta executar o comando abaixo com permissão de administrador (`sudo`):
```
make install
```

# Lista de Ferramentas:
- dsmcc-receive: The dsmcc-receive tool will extract a dsmcc file system from a transport stream file.
- eitsecactualtoanother: event information table to section
- ⭐ eitsecfilter: filtra .sec section, pega só certos pids
- eitsecmapper: mapeia onid tsid e sid a um onid2 tsid e sid2
- esaudio2pes: elementary stream (Elementary Stream) audio to packetized elementary stream (PES)
- esaudioinfo: ES audio info
- esvideompeg2info: ES video MPEG2 a PES
- esvideompeg2pes: ES video mpeg 2 to PES
- i13942ts: Dump .iso
- m2ts2cbrts: adds empty packets to input.ts to reach uniform output_bit/s, default is 48mbps
- mpe2sec: Create a tun device and send DVB/MPE DSM-CC sections to stdout.
- pes2es: PES to ES
- pes2txt: PES to digital teletext (TXT)
- pesaudio2ts: PES audio to TS. Tem função pra dar loop em áudio
- pesdata2ts: PES to TS
- ⭐ sec2ts: Section to TS. Uso: sec2ts PID < firstsdt.sec > firstsdt.ts
- ts2m2ts: TS to m2TS
- ts2pes: TS to PES
- ⭐ ts2sec: TS to SEC. Uso: ocdir1.ts 2003 > output.sec
- ⭐ tscbrmuxer: Multiplexa vários TSs em um só a bitrate constante (cbr).
- tsccc: check continuity counter errors and warnings
- tsdiscont: Checks for and fixes discontinuity problems
- tsdoubleoutput: Record output of ts
- ⭐ tsfilter: Escolhe quais PIDS do TS você quer ficar
- tsfixcc: Tsfixcc increases countinuity counter of every packet following each other without adapatation field parsing. Useful to link ts of sections in a single ts.
- tsinputswitch: Uma forma de alternar entre TSs dado um int
- tsloop: transforma um TS em um loop, útil pra criar um stream maior.
- ⭐ tsmask: Escolhe quais PIDS você quer remover
- ⭐ tsmodder: Muda os pacotes com certo PID pelos pacotes do TS escolhido.
- tsnullfiller: adiciona pacotes vazios pra atingir um certo bits/s
- tsnullshaper: Replace null packets from TS with packets from another TS. This suits anyway PSI insertion case that is not so time strict
- tsororts: ts packets are read from inputfile3.ts if they are not immediatly available from inputfile1.ts or inputfile2.ts'
- tsorts: ts packets are read from inputfile2.ts if they are not immediatly available from inputfile1.ts'
- tsoutputswitch: Switch que pode mostrar o TS na porta 1 ou 2, ou nas duas.
- tspcrmeasure: Aprende o bitrate de um TS.
- tspcrrestamp: Restampa os PCRs dos PES de um TS
- tspcrstamp: Conserta o PCR de um ts
- ⭐ tspidmapper: Muda o PID de um ts pra outro PID.
- tsstamp: Ajeita os valores PCR/PTS/DTS.
- tstcpreceive: Recebe TS por TCP
- tstcpsend: Envia TS por TCP
- tstdt: Add time info to TS:
- tstimedwrite: Writes TS to output TS at a certain bit rate
- tstimeout: Switches to backup TS if input TS times out.
- tsudreceive: Receive TS from UDP
- tsudpsend: Send TS from UDP
- tsvbr2cbr: Converts TS with Variable Bit Rate (VBR) to CBR by adding empty packets.
- txt2pes: Teletext (TXT) to PES.
- zpipe: pipes source to destination.

# Outras Ferramentas
- DVBSnoop facilita a leitura rápida de arquivos .sec e .ts. O comando abaixo lê a PAT de um arquivo .sec:
```
dvbsnoop -tsraw -s sec -tssubdecode -if pat.sec -N 2 0
```

# Comandos comuns
- `ts2sec pattaya-aerial-view30.ts 0 > pattaya-pat.sec`: Obtem todas as seções do TS com o PID 0, armazenando num arquivo.sec
- `dvbsnoop -tsraw -s sec -if pattaya-pat.sec -n 1 0`: Analisa a tabela a primeira tabela PAT que aparece no TS.
