s="\033[s"
u="\033[u"

# Position of column
# As per my command prompt, i want 15th column( so 14C)
pos="\033[1000D\033[14C"
while [ : ]
do
    eval echo -ne '$s$pos\|$u'
    sleep 0.3
    eval echo -ne '$s$pos/$u'
    sleep 0.3
    eval echo -ne '$s$pos一$u'
    sleep 0.3
    eval echo -ne '$s$pos\\\\$u'
    sleep 0.3
    eval echo -ne '$s$pos\|$u'
    sleep 0.3
    eval echo -ne '$s$pos\$$u'
    sleep 0.3
done
