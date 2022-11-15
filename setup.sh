mkdir -p ~/.streamlit/
echo "\[server]\n\
email =\" edo.hanifauzan.satria@yahoo.com\"\n\
" >
~/.streamlit/credentials.toml
echo "\
[server]\n\
headless=true\n\
enableCORS=false\n\
port=$PORT\n\
" > ~/.streamlit/config.toml
