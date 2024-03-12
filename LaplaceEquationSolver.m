%laplace på rektangel
LY=100; %setter lengden på side i y-retning
LX=100; %lengde på side x-retning
u=zeros(LY,LX); 

colormap("cool");

teller = 0;

%%setter randverdier.
u(1,:) = 0; %top = 0
u(LY, :) = 0; %bunn = 0
u(:, 1) = 1; %venstre side = 1
u(:, LX) = 1; %høyre side = 1


while(teller<1000)
    teller = teller +1;
    %lager nytt bilde for hver tiende iterasjon
    if(mod(teller,10)==0)
        imagesc(u);
        colorbar;
        drawnow;
    end

    %oppdaterer u inni rektangelelet. 
    Au=u;
    for i=2: LY-1
        for j=2: LX-1
            Au(i,j)= (1/4)*(u(i,j+1)+u(i-1,j)+u(i+1,j)+u(i, j-1));
        end
    end
    u(2:LY-1,2:LX-1)= Au(2:LY-1, 2:LX-1);
end
