def slice_bytes(start, length, *bytes_data):
  num_bits = len(bytes_data) * 8
   
  end = start + length
   
  # if end > num_bits:
  #   raise ValueError("The end value is (%d) is larger than the number of bits passed (%d)" % (num_bits, num_bits))
   
  concatenated_bytes = b''.join(bytes_data)
  integer_value = int(concatenated_bytes.encode('hex'), 16)
   
  integer_string = format(integer_value, '0%db' % num_bits)
  sliced_integer = int(integer_string[start:end], 2)
  return sliced_integer