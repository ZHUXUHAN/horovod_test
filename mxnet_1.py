#主要实现的是symbol_group的方法
import mxnet as mx
A=mx.symbol.Variable('A')
B=mx.symbol.Variable('B')
C=A*B
D=mx.symbol.Variable('D')
E=C+D
G=mx.symbol.Group([E,C])


a=mx.nd.empty(1)
b=mx.nd.ones(1)
d=mx.nd.ones(1)
excextor=G.bind(ctx=mx.cpu(), args={'A':a, 'B':b, 'D':d})
a[:]=10
excextor.forward()
e_out = excextor.outputs[0]
c_out = excextor.outputs[1]

print(e_out, c_out)


# dgraph=mx.viz.plot_network(symbol=G,title='model',save_format='pdf')
# dgraph.view()