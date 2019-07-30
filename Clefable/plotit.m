C=load('Clef vs Celesteela.txt');
n=linspace(1,length(C),length(C))';
rate=C./n;
plot(n,rate);
disp(['Celesteela wins ',int2str(C(end)),' in ',int2str(length(C)),' games']);
