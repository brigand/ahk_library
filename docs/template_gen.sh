mkdir $1
mkdir $1/_posts

while :
do
    echo "Name of file: "
    read fn
    cp 1970-01-01-template.md "$1/_posts/1970-01-01-$fn.md" 
done

