a
    ��_�  �                   @   s:   ddd�Z ddd�Zdd	� Zddd�Zdd� Zdd� ZdS )�=�*   c                 C   s   t | � | � dS )u�   [Cria uma linha]

    Args:
        simb (str, optional): [O símbolo que Vai Formar a linha]. Defaults to '='.
        tam (int, optional): [Tamanho da Linha]. Defaults to 42.
    Criado por:
        Murilo_Henrique060
    N)�print)�simb�tam� r   �n   c:\Users\Ivone\Desktop\tentando-criar-um-jogo-da-forca\forca\modulo\tratamento_de_strings\coisas_estéticas.py�linha   s    	r   �   ESCREVA O CABEÇALHO�    c                 C   s|   |dkr@t | � t|�d � td|� �� t | � t|�d � n8t | � |� td|t|� d  � |� �� t | � |� dS )u�  [Cria um Cabeçalho, com uma linha em cima, o texto e uma linha em baixo.]

    Args:
        simb (str, optional): [O símbolo que vai formar as linhas]. Defaults to '='.
        txt (str, optional): [O texto Do Cabeçalho]. Defaults to 'ESCREVA O CABEÇALHO'.
        tam (int, optional): [O tamanho do cabeçalho, 0 = acompanha o tamanho do texto]. Defaults to 0
    Criado por:
        Murilo_Henrique060
    r
   �   z  � �   N)r   �lenr   )r   Ztxtr   r   r   r   �
   cabeçalho   s    
 r   c                 C   s0   zt t| ��}W n   td� Y q 0 |S q d S )Nu'   ERRO! Digite um número inteiro válido)�int�inputr   )Ztexto�numeror   r   r   �leiaInt   s
    r   �   �   ERRO! Número Fora Do Alcance.Fc                 C   sZ   |rddl m} |�  d}t||d �D ]}|| kr(|d7 }q(|dkrRt|� dS dS dS )u8  [Verifica se Um Número Está Dentro de um Range.]

    Args:
        numero (int, optional): [Númaero à Ser Verificado.]. Defaults to 0.
        n1 (int, optional): [começo do range]. Defaults to 0.
        n2 (int, optional): [final do range]. Defaults to 1.
        outRange (str, optional): [Mensagem se o número Estiver Fora do Range]. Defaults to 'ERRO! Número Fora Do Alcance.'.
        cor (bool, optional): [Adicionar ou Não Cores]. Defaults to False.

    Returns:
        [bool]: [retorna True ou False]
    Criado por:
        Murilo_Henrique060
    r
   )�initr   FTN)Zcoloramar   �ranger   )r   Zn1Zn2ZoutRangeZcorr   �v�nr   r   r   �leiaInRange%   s    
r   c                 C   sd   t d|d� d}| D ]}t|� d|� �� |d7 }qtdd� td�}t|dt| ��}|r>|S q>d S )Nr   r   r   z - u   Sua Opção: )r   r   r   r   r   r   )�listaZ	cabecalho�c�itens�opc�rr   r   r   �menu@   s    

r    c                   C   s   t dd�� t�  t d� d S )NZREGRASz^42ux	  Palavras:
    As palavras do jogo da forca são guardadas em um arquivo de texto chamado 'palavras.txt', podem ser mudadas no menu principal
    ps: as palavras devem ser escritas sem acento.
O Jogo:
    o jogo começa sorteando uma palavra do banco de palavras, e mostra um hub:
                                                                        
    |======|                                                            
    |                                                                   
    |                                                                   
    |                                                                   
    |           _ _ _ _ _ _ _                                                        
  =====
    e a cada erro ele mostra uma parte do corpo (cabeça, tronco, braço direito, braço esquerdo, perna esquera, perna direita. Nessa ordem.)
    até completar o corpo inteiro como o abaixo:
                                                                        
    |======|                                                            
    |      o                                                             
    |     /|\                                                            
    |     / \                                                             
    |           _ _ _ _ _ _ _                                                        
  =====
    e a cada acerto o '_' é trocado pela letra escolhida:
                                                                        
    |======|                                                            
    |                                                                   
    |                                                                   
    |                                                                   
    |           _ A _ A _ _ A                                                        
  =====
    e quando você perde aparece:
                                                                        
    |======|                                                            
    |      o          VOCÊ PERDEU!!!                                                   
    |     /|\                                                            
    |     / \                                                             
    |           P A L A V R A                                                        
  =====)r   r   r   r   r   r   �regrasM   s    r!   N)r   r   )r   r	   r
   )r
   r
   r   r   F)r   r   r   r   r    r!   r   r   r   r   �<module>   s
   



