from dvbobjects.PSI.PAT import program_association_section, program_loop_item
from utils import slice_bytes

TABLE_ID_BITS = 8
SECTION_SYNTAX_INDICATOR_BITS = 1
SECTION_LENGTH_BITS = 12
TRANSPORT_STREAM_ID_BITS = 16
VERSION_NUMBER_BITS = 5
CURRENT_NEXT_INDICATOR_BITS = 1
SECTION_NUMBER_BITS = 8
LAST_SECTION_NUMBER_BITS = 8

PROGRAM_NUMBER_BITS = 16
NETWORK_PID_BITS = 13
PROGRAM_MAP_PID_BITS = 13

CRC32_BITS = 32

def main():
  with open("pat.sec", "rb") as f:
    data = f.read()
   
  table_id = slice_bytes(0, TABLE_ID_BITS, data[0])
  print("table_id: {:0} (0x{:02x})".format(table_id, table_id))
  section_syntax_indicator = slice_bytes(0, SECTION_SYNTAX_INDICATOR_BITS, data[1])
  print("section_syntax_indicator: {:0} (0x{:02x})".format(section_syntax_indicator, section_syntax_indicator))
  section_length = slice_bytes(4, SECTION_LENGTH_BITS, data[1:3])
  print("section_length: {:0} (0x{:04x})".format(section_length, section_length))
  transport_stream_id = slice_bytes(0, TRANSPORT_STREAM_ID_BITS, data[3:5])
  print("transport_stream_id: {:0} (0x{:04x})".format(transport_stream_id, transport_stream_id))
  version_number = slice_bytes(2, VERSION_NUMBER_BITS, data[5])
  print("version_number: {:0} (0x{:02x})".format(version_number, version_number))
  current_next_indicator = slice_bytes(6, CURRENT_NEXT_INDICATOR_BITS, data[5])
  print("current_next_indicator: {:0} (0x{:02x})".format(current_next_indicator, current_next_indicator))
  section_number = slice_bytes(6, SECTION_NUMBER_BITS, data[6])
  print("section_number: {:0} (0x{:02x})".format(section_number, section_number))
  last_section_number = slice_bytes(6, LAST_SECTION_NUMBER_BITS, data[7])
  print("last_section_number: {:0} (0x{:02x})".format(last_section_number, last_section_number))
  
  # section_length tells the number of bytes immediately after section_length, including the crc bytes.
  # Here we subtract the rest of the header and crc bytes, resulting in a multiple of
  num_header_bytes = (7 - 2) 
  num_crc_bytes = CRC32_BITS // 8
  num_loop_bytes = section_length - num_header_bytes - num_crc_bytes
  
  iterations = num_loop_bytes // 4
  
  program_loop = []
  offset = 8
  for i in range(iterations):
    program_number = slice_bytes(0, PROGRAM_NUMBER_BITS, data[offset:offset+2])
    print("    program_number: {:0} (0x{:04x})".format(program_number, program_number))
    if program_number == ord(u"0"):
      PID = slice_bytes(3, NETWORK_PID_BITS, data[offset+2:offset+4])
      print("    network_PID: {:0} (0x{:04x})".format(PID, PID))
    else:
      PID = slice_bytes(3, PROGRAM_MAP_PID_BITS, data[offset+2:offset+4])
      print("    program_map_PID: {:0} (0x{:04x})".format(PID, PID))
    print("")
    
    program_loop.append(program_loop_item(
      program_number = program_number,
      PID = PID  
    )) 
    offset += 4
  
  pat = program_association_section(
	      transport_stream_id = transport_stream_id,
        program_loop = program_loop,
        version_number = version_number + 1, # you need to change the table number every time you edit, so the decoder will compare its version with the new one and update the table
        section_number = section_number,
        last_section_number = last_section_number
  )
  
  out = open("./pat2.sec", "wb")
  out.write(pat.pack())
  out.close
  out = open("./pat2.sec", "wb") # python   flush bug
  # out.close
  # os.system('/usr/local/bin/sec2ts 0 < ./pat.sec > ./firstpat.ts')

if __name__ == "__main__":
  main()