from langchain_text_splitters import CharacterTextSplitter
from langchain

text = '4 pieces of Galouti Kebab usually have around 20–28g protein total, depending on the meat and size. Approx breakdown: 1 medium galouti kebab → ~5–7g protein. 4 kebabs → ~20–28g protein. If they’re made with more mutton fat, protein can be slightly lower. Chicken versions are usually leaner and may give a bit more protein.'

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_text(text)

print(result)