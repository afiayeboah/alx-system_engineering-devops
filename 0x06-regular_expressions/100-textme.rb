#!/usr/bin/env ruby
SENDER = ARGV[0].scan(/from:\+*\w*/).join[2..-1]
RECEIVER = ARGV[0].scan(/to:\+*\w*/).join[4..-1]
FLAGS = ARGV[0].scan(/flags:(.*?)\]/).join

message = "#{SENDER},#{RECEIVER},#{FLAGS}"
puts message
