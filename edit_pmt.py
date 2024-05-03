from dvbobjects.PSI.PMT import program_map_section, stream_loop_item

table_id = 0x3
section_max_size = 1024

pmt = program_map_section(table_id, section_max_size)

print(pmt.table_id)

pmt.table_id = 0x5

print(pmt.table_id)