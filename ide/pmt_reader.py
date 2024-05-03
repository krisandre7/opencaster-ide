import os
from dvbobjects.PSI.PMT import program_map_section, stream_loop_item
from utils import slice_bytes

TABLE_ID_BITS = 8
SECTION_SYNTAX_INDICATOR_BITS = 1
SECTION_LENGTH_BITS = 12
PROGRAM_NUMBER_BITS = 16
VERSION_NUMBER_BITS = 5
CURRENT_NEXT_INDICATOR_BITS = 1
SECTION_NUMBER_BITS = 8
LAST_SECTION_NUMBER_BITS = 8
PCR_PID_BITS = 13
PROGRAM_INFO_LENGTH_BITS = 12

STREAM_TYPE_BITS = 8
ELEMENTARY_PID = 13
ES_INFO_LENGTH_BITS = 12

CRC32_BITS = 32

def main():
  # TODO: Caminho pro arquivo precisa ser argumento e ter validacao se caminho nao existe
  with open("pmt.sec", "rb") as f:
    data = f.read()
  
  # TODO: Nao pode ser hardcoded
  PMT_PID = 1031
   
  table_id = slice_bytes(0, TABLE_ID_BITS, data[0])
  print("table_id: {:0} (0x{:02x})".format(table_id, table_id))
  
  section_syntax_indicator = slice_bytes(0, SECTION_SYNTAX_INDICATOR_BITS, data[1])
  print("section_syntax_indicator: {:0} (0x{:02x})".format(section_syntax_indicator, section_syntax_indicator))
  
  section_length = slice_bytes(4, SECTION_LENGTH_BITS, data[1:3])
  print("section_length: {:0} (0x{:04x})".format(section_length, section_length))
  
  program_number = slice_bytes(0, PROGRAM_NUMBER_BITS, data[3:5])
  print("program_number: {:0} (0x{:04x})".format(program_number, program_number))
  
  version_number = slice_bytes(2, VERSION_NUMBER_BITS, data[5])
  print("version_number: {:0} (0x{:02x})".format(version_number, version_number))
  
  current_next_indicator = slice_bytes(6, CURRENT_NEXT_INDICATOR_BITS, data[5])
  print("current_next_indicator: {:0} (0x{:02x})".format(current_next_indicator, current_next_indicator))
  
  section_number = slice_bytes(6, SECTION_NUMBER_BITS, data[6])
  print("section_number: {:0} (0x{:02x})".format(section_number, section_number))
  
  last_section_number = slice_bytes(6, LAST_SECTION_NUMBER_BITS, data[7])
  print("last_section_number: {:0} (0x{:02x})".format(last_section_number, last_section_number))
  
  pcr_pid = slice_bytes(4, PCR_PID_BITS, data[8:10])
  print("pcr_pid: {:0} (0x{:04x})".format(pcr_pid, pcr_pid))
  
  program_info_length = slice_bytes(4, PROGRAM_INFO_LENGTH_BITS, data[10:12])
  print("program_info_length: {:0} (0x{:04x})".format(program_info_length, program_info_length))
  
  # section_length tells the number of bytes immediately after section_length, including the crc bytes.
  # Here we subtract the rest of the header and crc bytes, resulting in a multiple of
  num_header_bytes = (11 - 2) 
  num_crc_bytes = 4
  num_loop_bytes = section_length - num_header_bytes - num_crc_bytes
  
  iterations = num_loop_bytes // 4
  
  # TODO: Implementa descritores
  program_info_descriptor_loop = []
  decriptor_loop = []
  stream_loop = []
  offset = 12
  for i in range(iterations):
    stream_type = slice_bytes(0, STREAM_TYPE_BITS, data[offset])
    print("    stream_type: {:0} (0x{:02x})".format(stream_type, stream_type))
    
    elementary_pid = slice_bytes(3, ELEMENTARY_PID, data[offset+1:offset+3])
    print("    elementary_pid: {:0} (0x{:04x})".format(elementary_pid, elementary_pid))
    
    es_info_length = slice_bytes(5, ES_INFO_LENGTH_BITS, data[offset+3:offset+5])
    print("    es_info_length: {:0} (0x{:04x})".format(es_info_length, es_info_length))
    print("")
    
    # TODO: Implementar descritor
    element_info_descriptor_loop = []
    stream_loop.append(
      stream_loop_item(
        stream_type = stream_type, # mpeg2 video stream type
        elementary_PID = elementary_pid,
        element_info_descriptor_loop = element_info_descriptor_loop
      )
    )
    offset += 5
  
  pmt = program_map_section(
    program_number = program_number,
    PCR_PID = pcr_pid,
    program_info_descriptor_loop = program_info_descriptor_loop,
    stream_loop = stream_loop,
    version_number = version_number + 1, # you need to change the table number every time you edit, so the decoder will compare its version with the new one and update the table
    section_number = section_number,
    last_section_number = last_section_number,
  )   
  
  out = open("./pmt2.sec", "wb")
  out.write(pmt.pack())
  out.close
  out = open("./pmt2.sec", "wb") # python   flush bug
  out.close
if __name__ == "__main__":
  main()