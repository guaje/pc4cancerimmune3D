from ipywidgets import Output
from IPython.display import HTML, Javascript, display


class FuryTab(object):

    def __init__(self):
        self.tab = Output(layout={'height': '600px'})
        #self.tab = Output(layout={'height': 'auto'})
        #self.tab.append_display_data(HTML(filename='doc/fury_client.html'))
        #self.tab.append_display_data(Javascript(
        #    filename='doc/FuryWebClient.js'))
        html = \
            """
            <iframe 
                src='http://fury.grg.sice.indiana.edu/tumor/'
                height='500' width='100%'>
            </iframe>
            """
        html = \
            """
            <iframe src='doc/fury_client.html' height='500' width='100%'>
            </iframe>
            """
        self.tab.append_display_data(HTML(html))
        js = \
            """
            element.css({backgroundColor: "gray", margin: "0px", 
                         padding: "0px"});
            element.height(100);
            element.width(100);
            element.html( $( "<div id='fury'></div>" ) );
            
            const newScriptTag = document.createElement('script');
            newScriptTag.type = 'text/javascript';
            newScriptTag.src = 'doc/FuryWebClient.js';
            document.body.appendChild(newScriptTag);
            """
        #self.tab.append_display_data(Javascript(js))
        #self.tab.append_display_data(Javascript(filename='doc/FuryWebClient.js'))
