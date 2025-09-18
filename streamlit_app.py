import streamlit as st
import pandas as pd
from main2 import get_search_results

st.title("Market Research Tool")

# Search input
query = st.text_input("Enter your search query:")

if st.button("Search"):
    if query:
        with st.spinner("Searching..."):
            results = get_search_results(query)
            st.write("Debug - Raw results:", results)  # Debug output
            
            if "error" in results:
                st.error(f"Error: {results['error']}")
            else:
                # Content display
                st.markdown("### Search Results")
                if results.get("content"):
                    st.markdown(results["content"])
                    
                    # Citations section
                    if results.get("annotations"):
                        st.markdown("#### Citations")
                        for annotation in results["annotations"]:
                            if annotation["type"] == "url_citation":
                                citation = annotation["url_citation"]
                                st.markdown(f"""
                                - **Source:** [{citation['title']}]({citation['url']})
                                - **Quote:** _{citation['exactQuote']}_
                                """)
                
                # URLs section (in columns)
                col1, col2 = st.columns(2)
                
                with col1:
                    if results.get("visitedURLs"):
                        st.markdown("### Visited URLs")
                        urls_df = pd.DataFrame(results["visitedURLs"], columns=["URL"])
                        st.dataframe(urls_df, height=300)
                
                with col2:
                    if results.get("readURLs"):
                        st.markdown("### Read URLs")
                        read_urls_df = pd.DataFrame(results["readURLs"], columns=["URL"])
                        st.dataframe(read_urls_df, height=300)
                
                # Stats
                st.markdown(f"Total URLs processed: {results.get('numURLs', 0)}")
                
                # if results.get("usage"):
                #     st.markdown("### Usage Statistics")
                #     st.json(results["usage"])
    else:
        st.warning("Please enter a search query")
