def linha_vazia():
    print()
class Canal:
    def __init__(self, nome, descricao, inscritos):
        self.nome = nome
        self.descricao = descricao
        self.inscritos = inscritos
        self.videos = []
        self.playlists = []
    def inscrever(self, quantidade = 1):
        self.inscritos += quantidade
    def postar(self, video):
        if video in self.videos:
            print('esse vídeo já foi postado!')
            return
        self.videos.append(video)
    def adicionar_palylist(self, playlist):
        if playlist in self.playlists:
            print('essa playlist já foi adicionada!')
            return 
        self.playlists.append(playlist)
    def visualizar_playlist(self):
        for playlist in self.playlists:
           linha_vazia()
           print(f'TÍTULO DA PLAYLIST: {playlist.titulo}')
           linha_vazia()
           print('VÍDEOS')
           linha_vazia()
           playlist.visualizar()
           linha_vazia()
class CanalEmpresarial(Canal):
    def __init__(self, nome, descricao, inscritos):
        super().__init__(nome, descricao, inscritos)
        self._equipe = []
    @property
    def equipe(self):
        return self._equipe
    def adicionar_membro_da_equipe(self, membro):
        if membro not in self._equipe:
            self._equipe.append(membro)
        else:
            print(f'{membro} já está na equipe!')
    def remover_membro_da_equipe(self, membro):
        if membro in self._equipe:
            self._equipe.remove(membro)
        else:
            print(f'{membro} não está na equipe')
class Video:
    def __init__(self, nome, descricao, data):
        self.nome = nome 
        self.descicao = descricao
        self.visualizacoes = 0
        self.likes = 0
        self.deslikes = 0
        self.comentarios = []
        self.data = data
    def __repr__(self):
        return f'<{self.nome}>'
    def assistir(self):
        self.visualizacoes += 1
    def gostei(self):
        self.likes += 1
    def nao_gostei(self):
        self.deslikes += 1
    def comentar(self, comentario):
        self.comentarios.append(comentario)
    def info(self):
        print(f"""título: {self.nome} 
descrição: {self.descicao} 
{self. visualizacoes} visualizações 
{self.likes} likes 
{self.deslikes} deslikes 
{self.comentarios}\n""")
class Playlist:
    def __init__(self, titulo):
        self.titulo = titulo 
        self.lista_de_videos = []
    def adicionar(self, video):
        self.lista_de_videos.append(video)
    def visualizar(self):
        for video in self.lista_de_videos:
            video.info()
            print()
canal_conectado = Canal('Conectado', 'Política de Entretenimento, aqui você se informa e se diverte.', 734000)
canal_guanabara = Canal('Curso em Vídeo', 'O seu curso de tecnologia favorito.', 2630000)
canal_duolingo = CanalEmpresarial('Duolingo', 'inglês', 500000)
video_poo = Video('Python orientado a objetos', 'Aprenda agora', '06/01/2026')
canal_guanabara.postar(video_poo)
playlist1 = Playlist('Assistir mais tarde')
playlist1.adicionar(video_poo)
#playlist1.visualizar()
video_poo.comentar('primero')
video_poo.comentar('segundo')
canal_guanabara.adicionar_palylist(playlist1)
canal_guanabara.visualizar_playlist()
