#!/usr/bin/env ruby
from = ARGV[0].scan(/from:[+?a-zA-Z0-9]+/).join()
to = ARGV[0].scan(/to:[+?a-zA-Z0-9]+/).join()
flags = ARGV[0].scan(/flags:[-:+0-9]*/).join()
output = from[5..-1] + "," +  to[3..-1] + "," + flags[6..-1]
puts output
