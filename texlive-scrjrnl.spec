Name:		texlive-scrjrnl
Version:	74998
Release:	1
Summary:	Typeset diaries or journals
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/scrjrnl
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scrjrnl.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scrjrnl.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scrjrnl.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A class, based on scrbook, designed for typesetting diaries,
journals or devotionals.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/scrjrnl/scrjrnl.cls
%doc %{_texmfdistdir}/doc/latex/scrjrnl/README
%doc %{_texmfdistdir}/doc/latex/scrjrnl/example.pdf
%doc %{_texmfdistdir}/doc/latex/scrjrnl/scrjrnl.pdf
#- source
%doc %{_texmfdistdir}/source/latex/scrjrnl/scrjrnl.dtx
%doc %{_texmfdistdir}/source/latex/scrjrnl/scrjrnl.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
