#!/usr/bin/env ruby

i = 0
loop do
  i += 1
  n = (i * 5) + 1
  puts "Trying n=#{n}"

  n1_numerator = (4 * n) - 4
  next if n1_numerator % 5 != 0
  n1 = n1_numerator / 5
  next if n1 % 5 != 1

  n2_numerator = (4 * n1) - 4
  next if n2_numerator % 5 != 0
  n2 = n2_numerator / 5
  next if n2 % 5 != 1

  n3_numerator = (4 * n2) - 4
  next if n3_numerator % 5 != 0
  n3 = n3_numerator / 5
  next if n3 % 5 != 1

  n4_numerator = (4 * n3) - 4
  next if n4_numerator % 5 != 0
  n4 = n4_numerator / 5
  next if n4 % 5 != 1

  n5_numerator = (4 * n4) - 4
  next if n5_numerator % 5 != 0
  n5 = n5_numerator / 5
  next if n5 % 5 != 1
  
  puts "Solution: n=#{n}"
  break
end

