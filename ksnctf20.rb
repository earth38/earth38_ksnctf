require "bigdecimal/math"
require "prime"

#円周率1000桁を取得
pi = BigMath::PI(1000)
pi = pi.to_s 

#取得した円周率を10文字ずつ抜き出して素数かどうかを判定する
for i in 1..1000 do
    n = pi[i,10].to_i
    if Prime.prime?(n) then
        puts "FLAG_Q20_" + pi[i,10]
        exit
    end
end
