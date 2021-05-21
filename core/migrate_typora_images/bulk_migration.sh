OIFS="$IFS"
IFS=$'\n'
for file in $(ls *.md)  
do
     echo $file
     python3 /home/yurii/Programming/Python3/datacamp/core/migrate_typora_images/migrate_typora_images.py --filename $file
done
IFS="$OIFS"

# https://unix.stackexchange.com/questions/9496/looping-through-files-with-spaces-in-the-names

